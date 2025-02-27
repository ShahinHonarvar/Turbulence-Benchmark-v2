def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(5, 9) if s[i].isalpha()))
    palindromes = set()
    for length in range(3, min(len(letters), 5) + 1):
        for char in letters:
            palindrome = char * length
            if palindrome[0] != palindrome[-1] and palindrome in palindromes:
                continue
            palindromes.add(palindrome)
            for perm in itertools.permutations(letters - {char}, length - 1):
                palindrome = char + ''.join(perm) + char
                if palindrome[0] != palindrome[-1] and palindrome in palindromes:
                    continue
                palindromes.add(palindrome)
    return palindromes