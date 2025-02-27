def palindromes_between_indices(string):
    letters = []
    for i in range(1, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters) - j + 1):
                permutation = letters[i:j]
                for l in range(k + 1):
                    permutation_copy = permutation.copy()
                    for m in range(k):
                        permutation_copy.insert(l, letters[j - 1 - m])
                    if len(permutation_copy) >= 5:
                        palindrome = ''.join(permutation_copy)
                        if palindrome == palindrome[::-1]:
                            result.add(palindrome)
    return result