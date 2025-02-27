def palindromes_between_indices(s):
    s = s[1:8].lower()
    s_set = set(s)
    palindromes = set()
    for char in s_set:
        for other_char in s_set:
            if char != other_char:
                palindrome = char * 4 + other_char + char * 4
                palindromes.add(palindrome)
    for char in s_set:
        palindrome = char * 7
        palindromes.add(palindrome)
    return palindromes