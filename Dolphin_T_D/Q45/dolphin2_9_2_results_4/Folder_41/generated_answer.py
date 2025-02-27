def palindromes_between_indices(s):
    letters = s[2:4]
    combinations = set()
    for i in range(len(letters)):
        for j in range(len(letters)):
            for k in range(len(letters)):
                palindrome = letters[i] + letters[j] + letters[k]
                if palindrome == palindrome[::-1]:
                    combinations.add(palindrome)
    return combinations