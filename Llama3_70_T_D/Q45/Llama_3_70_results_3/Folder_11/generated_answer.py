def palindromes_between_indices(s):
    sub_string = s[3:8].lower()
    letters = [char for char in sub_string if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            sub_sub_string = letters[i:i + length]
            for j in range(len(sub_sub_string) // 2):
                if sub_sub_string[j] != sub_sub_string[-j - 1]:
                    break
            else:
                palindrome = ''.join(sub_sub_string)
                palindromes.add(palindrome)
    return palindromes