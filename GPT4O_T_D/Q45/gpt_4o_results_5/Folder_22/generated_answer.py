def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub = s[5:7]
    freq = {}
    for char in sub:
        if char.isalpha():
            lower_char = char.lower()
            freq[lower_char] = freq.get(lower_char, 0) + 1

    def generate_palindromes(half, middle, length, result):
        if len(half) == length // 2:
            palindrome = half + middle + half[::-1]
            result.add(palindrome)
            return
        for char in list(freq.keys()):
            if freq[char] > 1:
                freq[char] -= 2
                generate_palindromes(half + char, middle, length, result)
                freq[char] += 2
            elif length % 2 == 1 and freq[char] == 1 and (not middle):
                freq[char] -= 1
                generate_palindromes(half, char, length, result)
                freq[char] += 1
    result = set()
    for length in range(3, len(sub) + 1):
        generate_palindromes('', '', length, result)
    return result