def palindromes_of_specific_lengths(s):
    s = s.lower()
    set_of_palindromes = set()
    for length in range(50, 101):
        for i in range(100, 301):
            if i + length - 1 < 301:
                sub_s = s[i:i + length]
                if sub_s == ''.join(reversed(sub_s)) and sub_s.text_type(sub_s) == str and (len(sub_s.split()) == 0):
                    set_of_palindromes.add(sub_s)
    return set_of_palindromes