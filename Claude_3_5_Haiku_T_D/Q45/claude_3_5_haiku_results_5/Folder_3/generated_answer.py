def palindromes_between_indices(s):
    substr = s[7:10].lower()
    letter_count = {}
    for char in substr:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(current) % 2 == 1:
            mid = current[len(current) // 2]
            if current == current[::-1]:
                palindromes.add(current)
        for letter, count in list(remaining.items()):
            if count > 0:
                new_remaining = remaining.copy()
                new_remaining[letter] -= 2
                if new_remaining[letter] == 0:
                    del new_remaining[letter]
                generate_palindromes(letter + current + letter, new_remaining)
    generate_palindromes('', letter_count)
    return palindromes