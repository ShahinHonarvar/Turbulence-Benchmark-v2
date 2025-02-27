def palindromes_between_indices(str):
    chars = [c.lower() for c in str[4:9] if c.isalpha()]
    result = set()
    for arr in permutations(chars, len(chars)):
        for i in range(len(arr)):
            for j in range(i + 2, len(arr) + 1):
                if arr[i:j] == arr[i:j][::-1]:
                    result.add(''.join(arr[i:j]))
    return result