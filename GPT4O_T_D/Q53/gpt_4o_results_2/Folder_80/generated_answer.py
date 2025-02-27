def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    valid_characters = [c for c in s.lower() if c.isalpha()]
    start = 0
    end = len(valid_characters)
    palindromes = set()
    while end - start >= 30:
        for i in range(start, end):
            for j in range(i + 30, end + 1):
                candidate = ''.join(valid_characters[i:j])
                if is_palindrome(candidate):
                    palindromes.add(candidate)
        start += 1
        end -= 1
    return palindromes