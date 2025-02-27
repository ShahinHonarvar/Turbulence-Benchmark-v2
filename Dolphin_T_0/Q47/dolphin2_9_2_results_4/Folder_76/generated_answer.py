def palindromes_of_specific_lengths(s):
    substring = s[100:293]
    set_of_palindromes = set()
    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and all((c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in segment)):
                set_of_palindromes.add(segment)
    return set_of_palindromes