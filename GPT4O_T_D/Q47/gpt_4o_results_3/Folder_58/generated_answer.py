def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    substr = s[125:284].lower()
    palindromes = set()
    for length in range(109, 127):
        for start in range(len(substr) - length + 1):
            seq = substr[start:start + length]
            filtered_seq = ''.join([char for char in seq if char.isalpha()])
            if len(filtered_seq) == length and is_palindrome(filtered_seq):
                palindromes.add(filtered_seq)
    return palindromes