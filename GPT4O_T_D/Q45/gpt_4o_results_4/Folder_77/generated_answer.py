def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 7:
        return set()
    substr = s[4:7]
    letter_counts = {}
    for char in substr:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    palindrome_set = set()

    def can_form_palindrome(chars, length):
        odd_count = 0
        for count in chars.values():
            if count % 2 != 0:
                odd_count += 1
        return odd_count <= 1 and sum(chars.values()) >= length

    def generate_palindrome(chars, path, length):
        if len(path) == length:
            palindrome_set.add(path)
            return
        for char in chars:
            if chars[char] > 1:
                chars[char] -= 2
                generate_palindrome(chars, char + path + char, length)
                chars[char] += 2
            elif chars[char] == 1 and len(path) == length - 1:
                palindrome_set.add(char + path)
    for length in range(4, sum(letter_counts.values()) + 1):
        if can_form_palindrome(letter_counts, length):
            generate_palindrome(letter_counts, '', length)
    return palindrome_set