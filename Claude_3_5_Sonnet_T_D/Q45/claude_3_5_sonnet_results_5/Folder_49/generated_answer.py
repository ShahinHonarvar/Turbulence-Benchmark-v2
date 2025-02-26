def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:8])).lower()

    def generate_palindromes(chars):
        if len(chars) <= 2:
            return set()
        result = set()
        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                for k in range(j + 1, len(chars)):
                    palindrome = chars[i] + chars[j] + chars[k] + chars[j] + chars[i]
                    result.add(palindrome)
        return result
    return generate_palindromes(letters)