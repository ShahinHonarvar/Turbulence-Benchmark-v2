import re
    from collections import defaultdict

def palindromes_of_specific_lengths(s: str) -> set[str]:
    english_letters_only = re.findall('[a-zA-Z]', s[155:284])
    length_filtered = defaultdict(str)
    for i in range(104, 121):
        length_filtered[i] = [english_letters_only[j:j + i] for j in range(len(english_letters_only) - i + 1) if english_letters_only[j:j + i] == english_letters_only[j:j + i][::-1]]
    return {word.lower() for length in length_filtered.values() for word in length if word}