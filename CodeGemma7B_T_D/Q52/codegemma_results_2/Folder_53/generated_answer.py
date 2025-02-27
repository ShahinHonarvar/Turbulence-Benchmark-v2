from collections import defaultdict

def palindrome_of_length_n(input_str):
    input_str = input_str.lower()
    result = set()
    store = defaultdict(list)
    for i in range(len(input_str)):
        for j in range(i + 67, len(input_str)):
            store[input_str[i:j + 1]].append(i)
    for key, indices in store.items():
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                if indices[i] + len(key) == indices[j]:
                    result.add(key)
    return result