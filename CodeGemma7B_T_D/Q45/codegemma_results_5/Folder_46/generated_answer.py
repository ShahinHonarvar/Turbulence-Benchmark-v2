def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    if text[4:10].isalpha():
        for i in itertools.permutations(text[4:10]):
            palindrome = ''.join(i)
            if palindrome in palindromes:
                continue
            palindromes.add(palindrome)
    return palindromes