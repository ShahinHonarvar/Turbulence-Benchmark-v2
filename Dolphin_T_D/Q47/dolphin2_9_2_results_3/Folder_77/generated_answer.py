def palindromes_of_specific_lengths(s):
    range_start = 103
    range_end = 276
    min_length = 100
    max_length = 169
    letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(range_start, range_end + 1):
        for length in range(min_length, max_length + 1):
            sub_s = s[i:i + length]
            if len(sub_s) != len(set(sub_s).intersection(letters)):
                continue
            else:
                sub_s = sub_s.lower()
                if sub_s == sub_s[::-1]:
                    palindromes.add(sub_s)
    return palindromes