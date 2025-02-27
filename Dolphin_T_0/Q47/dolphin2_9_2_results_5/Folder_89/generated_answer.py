def palindromes_of_specific_lengths(s):
    sub_s = s[17:89]
    result = set()
    for length in range(12, 15):
        for i in range(len(sub_s) - length + 1):
            sub_string = sub_s[i:i + length]
            mid_length = length // 2
            left = sub_string[:mid_length]
            right = sub_string[mid_length + 1:] if length % 2 == 0 else sub_string[mid_length + 1:length]
            if left.lower() == right.lower():
                result.add(sub_string)
    return result