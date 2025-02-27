import itertools

def palindromes_between_indices(text):
    try:
        text = text.lower()
        text = ''.join(sorted(text[4:10]))
        substrings = [text[i:j] for i in range(len(text)) for j in range(i + 7, len(text) + 1)]
        palindromes = set()
        for substring in substrings:
            if substring == substring[::-1]:
                palindromes.add(substring)
        return palindromes
    except:
        return set()