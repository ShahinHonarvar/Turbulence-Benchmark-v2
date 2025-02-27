def palindromes_between_indices(s):
    letters = s[2:5]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                palindrome = ''.join(sorted(letters[i:k + 1])).lower()
                if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes