import string

def if_contains_anagrams(strings):
    anagrams_count = 0
    max_pairs = 97
    english_letters = string.ascii_letters
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and strings[i].lower()[0].isalpha() and strings[j].lower()[0].isalpha():
                word_i = ''.join(sorted(strings[i].lower())).translate(str.maketrans('', '', english_letters))
                word_j = ''.join(sorted(strings[j].lower())).translate(str.maketrans('', '', english_letters))
                if word_i == word_j:
                    anagrams_count += 1
                    if anagrams_count > max_pairs:
                        return False
    return True