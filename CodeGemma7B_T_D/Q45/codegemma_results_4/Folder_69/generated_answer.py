from itertools import permutations as p

def palindromes_between_indices(text):
    text = text.lower()
    filtered_text = [c for c in text[0:4] if c.isalpha()]
    palindromes = set()
    for i in range(len(filtered_text) - 3):
        for j in range(i + 1, len(filtered_text) - 2):
            for k in range(j + 1, len(filtered_text) - 1):
                for l in range(k + 1, len(filtered_text)):
                    for perm in p(filtered_text[i:l + 1]):
                        palindrome = ''.join(perm)
                        palindromes.add(palindrome)
    return palindromes