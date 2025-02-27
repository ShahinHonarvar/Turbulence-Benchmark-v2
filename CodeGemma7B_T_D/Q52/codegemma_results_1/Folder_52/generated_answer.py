def palindrome_of_length_n(s):
    """Return the set of all palindromes of the length equal to n, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner."""
    sc = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            tmp = s[i:j]
            if tmp == tmp[::-1]:
                sc.add(tmp.lower())
    return sc