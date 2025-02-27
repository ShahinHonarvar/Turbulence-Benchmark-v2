def palindromes_between_indices(s):
    letters = set(s[7:9].lower()) - set(' ')
    result = set()
    for length in range(3, len(s) + 1):
        for c1 in letters:
            for c2 in letters:
                for c3 in letters:
                    if c1 != c2 or c1 != c3 or c2 != c3:
                        palindrome = c1 + c2 + c3
                        if palindrome == palindrome[::-1]:
                            result.add(palindrome)
    return result