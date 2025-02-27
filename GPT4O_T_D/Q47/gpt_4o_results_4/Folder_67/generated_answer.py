def palindromes_of_specific_lengths(s):
    s = s.lower()
    sub_str = s[65:100]
    results = set()
    for length in range(26, 34):
        for i in range(len(sub_str) - length + 1):
            slice_str = sub_str[i:i + length]
            letters_only = ''.join(filter(str.isalpha, slice_str))
            if letters_only == letters_only[::-1] and len(letters_only) == len(slice_str):
                results.add(slice_str)
    return results