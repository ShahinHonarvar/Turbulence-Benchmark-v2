def palindromes_between_indices(s):
    indices = list(map(str.lower, s[1:6]))
    palindrome_set = set()

    def is_palindrome(s):
        return s == s[::-1]
    for n in range(5, 0, -1):
        for i in range(len(indices)):
            for j in indices[i:i + n]:
                if is_palindrome(j):
                    palindrome_set.add(j)
    return palindrome_set