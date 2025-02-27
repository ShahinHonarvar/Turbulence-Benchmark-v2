from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    result = set()
    char_counts = defaultdict(int)
    for char in text:
        char_counts[char.lower()] += 1
        start, end = (len(text) - 1, len(text) - 1)
        l = 0
        while l < end:
            if char_counts.get(text[l].lower(), 0) == 0:
                l += 1
                continue
            if char_counts.get(text[end].lower(), 0) == 0:
                end -= 1
                continue
            if text[l].lower() != text[end].lower():
                break
            l += 1
            end -= 1
            if end - l + 1 >= 69:
                result.add(text[l:end + 1])
    return result