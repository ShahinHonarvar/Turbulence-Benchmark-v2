def palindromes_of_specific_lengths(s):
    substring = s[17:89].lower()
    set_palindromes = set()
    for i in range(len(substring)):
        for length in range(12, 15):
            temp_str = substring[i:i + length]
            if temp_str == temp_str[::-1] and temp_str.isalpha():
                set_palindromes.add(temp_str)
    return set_palindromes