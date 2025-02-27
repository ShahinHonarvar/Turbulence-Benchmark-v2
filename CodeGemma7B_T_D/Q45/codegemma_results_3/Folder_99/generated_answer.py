def palindromes_between_indices(text):
    palindromes = set()
    for i in range(4, 9):
        for j in range(i, 9):
            substring = text[i:j + 1]
            if substring.isalpha():
                permutations = itertools.permutations(substring)
                for permutation in permutations:
                    palindrome = ''.join(permutation)
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes