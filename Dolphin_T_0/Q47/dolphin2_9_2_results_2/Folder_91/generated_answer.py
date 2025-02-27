def palindromes_of_specific_lengths(s):
    s = s[:11].lower()
    lengths = [i for i in range(3, 6)]
    result_set = set()
    for i in lengths:
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i].isalpha():
                result_set.add(s[j:j + i])
    return result_set