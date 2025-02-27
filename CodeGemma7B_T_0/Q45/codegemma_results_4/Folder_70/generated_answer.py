import re
    import itertools

def palindromes_between_indices(text):
    text = text.lower()
    letters = re.findall('[a-zA-Z]', text)
    if len(letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 1, len(letters) - 2):
            for k in range(j + 1, len(letters) - 1):
                for l in range(k + 1, len(letters)):
                    palindrome = ''.join(itertools.permutations(letters[i:l + 1]))
                    if len(palindrome) >= 4:
                        palindromes.add(palindrome)
    return palindromes