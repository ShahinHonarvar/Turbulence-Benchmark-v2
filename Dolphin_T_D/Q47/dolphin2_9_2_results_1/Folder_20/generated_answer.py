def palindromes_of_specific_lengths(s):
    s = s[20:75].lower()
    set_palindromes = set()
    for length in range(36, 43):
        for i in range(0, length):
            temp = s[i:i + length]
            if temp == temp[::-1] and temp.isalpha():
                set_palindromes.add(temp)
    return set_palindromes