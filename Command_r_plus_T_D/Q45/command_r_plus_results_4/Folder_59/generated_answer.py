def palindromes_between_indices(s):
    s = s.lower()
    sub_str = s[8:10]
    unique_chars = set(sub_str)
    palindromes = set()
    for char in unique_chars:
        if sub_str.count(char) >= 2:
            palindromes.add(char * 2)
    return palindromes