def palindrome_of_length_at_least_n(s):
    s = s.lower()
    English_letters_set = set('abcdefghijklmnopqrstuvwxyz')
    length_s = len(s)
    palindromes_set = set()
    for length in range(35, length_s + 1):
        for i in range(0, length_s - length + 1):
            substring = s[i:i + length]
            if set(substring).issubset(English_letters_set) and substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set