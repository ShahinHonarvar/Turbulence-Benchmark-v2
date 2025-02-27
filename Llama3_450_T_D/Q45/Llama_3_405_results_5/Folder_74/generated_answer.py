def palindromes_between_indices(s):
    English_chars = [char.lower() for char in s[1:7] if 'a' <= char.lower() <= 'z']
    counts = {}
    for char in English_chars:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    all_palindromes = set()

    def generate_palindrome(current_str, counts, remaining_length):
        if remaining_length == 0:
            all_palindromes.add(current_str + current_str[::-1])
            return
        for char, count in counts.items():
            if count > 0:
                counts[char] -= 1
                generate_palindrome(current_str + char, counts, remaining_length - 1)
                counts[char] += 1
    for length in range(3, sum(counts.values()) + 1):
        generate_palindrome('', counts, length)
    return {palindrome for palindrome in all_palindromes if len(palindrome) >= 6}