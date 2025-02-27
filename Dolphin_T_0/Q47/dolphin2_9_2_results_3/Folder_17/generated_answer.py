def palindromes_of_specific_lengths(s):
    sub = s[22:96]
    lengths = [52, 53, 54, 55]
    valid_length_palindromes = []

    def is_palindrome(sub):
        for length in lengths:
            for i in range(len(sub)):
                if sub[i:i + length] == sub[i:i + length][::-1] and sub[i:i + length].isalpha():
                    valid_length_palindromes.append(sub[i:i + length])
    is_palindrome(sub)
    if valid_length_palindromes:
        return set(valid_length_palindromes)
    else:
        return set()