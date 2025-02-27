def palindromes_between_indices(string):
    chars = ''.join(sorted(string[4:10]))
    length = len(chars)
    palindromes = set()
    if length >= 5:
        for i in range(length):
            for j in range(length - i):
                sub_string_1 = chars[i:i + j + 1]
                sub_string_2 = sub_string_1[::-1]
                if sub_string_1 == sub_string_2 and len(sub_string_1) >= 5:
                    palindromes.add(sub_string_1.lower())
    return palindromes