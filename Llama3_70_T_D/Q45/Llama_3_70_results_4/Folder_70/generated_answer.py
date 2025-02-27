def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = sorted([c for c in s if c.isalpha()])
    result = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    palindrome = letters[i] + letters[j] + letters[k] + letters[l]
                    if palindrome == palindrome[::-1]:
                        result.add(palindrome)
    return result