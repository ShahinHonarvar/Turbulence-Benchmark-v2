def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    letters_between_indices = ''.join(filter(str.isalpha, s[:8].lower()))
    for i in range(len(letters_between_indices) - 3):
        for j in range(i + 1, len(letters_between_indices) - 2):
            for k in range(j + 1, len(letters_between_indices) - 1):
                for l in range(k + 1, len(letters_between_indices)):
                    palindrome = letters_between_indices[i:l + 1]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes