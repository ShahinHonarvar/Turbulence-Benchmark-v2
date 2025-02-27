def palindromes_of_specific_lengths(s):
    result_set = set()
    substring = s[10:76]
    for length in range(10, 21):
        for i in range(len(substring) - length + 1):
            sb = substring[i:i + length].lower()
            if sb == sb[::-1] and sb.isalpha():
                result_set.add(sb)
    return result_set