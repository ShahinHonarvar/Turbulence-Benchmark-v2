from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    palindromes = defaultdict(set)
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 40 and substring.isalpha():
                palindromes[len(substring)].add(substring.lower())
    return set((p for v in palindromes.values() for p in v))