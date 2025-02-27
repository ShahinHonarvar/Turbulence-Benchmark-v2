def palindromes_of_specific_lengths(s):
    palindromes = set()
    sub_string = s[10:75]
    lower_sub_string = ''.join([char for char in sub_string if char.isalpha()]).lower()
    for length in range(6, 9):
        for i in range(len(lower_sub_string) - length + 1):
            segment = lower_sub_string[i:i + length]
            if segment == segment[::-1]:
                palindromes.add(sub_string[i:i + length])
    return palindromes