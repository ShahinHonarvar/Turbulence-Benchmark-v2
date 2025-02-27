def palindromes_of_specific_lengths(s):
    """
    >>> palindromes_of_specific_lengths("A man, a plan, a canal: Panama")
    {'racecar', 'kayak'}
    >>> palindromes_of_specific_lengths("a")
    set()
    >>> palindromes_of_specific_lengths("abcdcba")
    {'abcdcba'}
    """
    return_set = set()
    s = s.lower()
    for i in range(24, 98):
        for j in range(i + 9, 98):
            for k in range(j - 1, i - 1, -1):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    return_set.add(s[i:j + 1])
    return return_set