def palindromes_of_specific_lengths(s):
    current_index = 103
    result = set()
    for i in range(current_index, 277):
        for j in range(i - 99, i + 1):
            s_reverse = s[j:i + 1][::-1]
            if s_reverse.isalpha() and s_reverse == s_reverse.lower():
                result.add(s_reverse)
    return result