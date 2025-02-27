from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    results = set()
    letters = defaultdict(list)
    for index, char in enumerate(string):
        char = char.lower()
        letters[char].append(index)
    for start in range(len(string)):
        for end in range(start + 94, len(string)):
            mid = (end - start) // 2
            left_part, right_part = (string[start:start + mid + 1], string[end - mid:end + 1])
            left_first, right_last = (left_part[0], right_part[-1])
            if left_first == right_last and all((char in letters.get(right_last) for char in left_part[1:-1])):
                results.add((start, end))
    return results