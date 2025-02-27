def palindrome_of_length_at_least_n(str):
    """
    This function returns the set of all palindromes of the
    length greater than or equal to 57 that exist in the
    given string. Each palindrome should only consist
    of English letters. If no such palindromes exist
    in the given string, the function should return an
    empty set. The function should find the palindromes
    in a case-insensitive manner.
    """
    str = str.lower()
    count = {}
    ans = set()
    for char in str:
        if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    for a in count.keys():
        for b in count.keys():
            if a != b:
                word = a + str(count[a]) + b
                if len(word) > 56:
                    ans.add(word)
    return ans