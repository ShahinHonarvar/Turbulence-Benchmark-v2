def palindromes_between_indices(s):

    def is_palindrome(check):
        return check == check[::-1]
    palindromes = set()
    for i in range(3, 6):
        if s[i] not in palindromes:
            palindromes.add(s[i].lower())
    length = 3
    while length <= len(palindromes):
        pal_set = set(itertools.combinations_with_replacement(palindromes, length))
        length += 1
        for v in pal_set:
            pal_string = ''.join(v)
            if is_palindrome(pal_string):
                palindromes.add(pal_string)
    return palindromes