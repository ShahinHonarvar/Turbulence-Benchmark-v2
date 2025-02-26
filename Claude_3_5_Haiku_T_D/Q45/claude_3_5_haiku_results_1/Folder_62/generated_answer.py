def palindromes_between_indices(s):

    def can_form_palindrome(freq):
        odd_count = sum((1 for count in freq.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(freq, length):

        def backtrack(current, remaining_freq):
            if len(current) == length:
                palindromes.add(current)
                return
            for char, count in list(remaining_freq.items()):
                if count > 0:
                    remaining_freq[char] -= 2
                    new_current = char + current + char
                    if remaining_freq[char] == 0:
                        del remaining_freq[char]
                    backtrack(new_current, remaining_freq)
                    if char in remaining_freq:
                        remaining_freq[char] += 2
                    else:
                        remaining_freq[char] = 2
        palindromes = set()
        backtrack('', freq)
        return palindromes
    letters = [c.lower() for c in s[:9] if c.isalpha()]
    freq = {}
    for letter in letters:
        freq[letter] = freq.get(letter, 0) + 1
    if not can_form_palindrome(freq):
        return set()
    palindrome_set = set()
    for length in range(7, len(letters) + 1, 2):
        palindrome_set.update(generate_palindromes(freq.copy(), length))
    return palindrome_set