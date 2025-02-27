def palindromes_of_specific_lengths(s):
    s = s[17:66].lower()
    set_of_palindromes = set()
    for length in range(23, 37):
        for index in range(len(s) - length + 1):
            sub_s = s[index:index + length]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                set_of_palindromes.add(sub_s)
    return set_of_palindromes