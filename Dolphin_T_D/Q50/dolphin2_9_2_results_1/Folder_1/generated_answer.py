def if_contains_anagrams(lst):

    def is_anagram(a: str, b: str) -> bool:
        a = a.lower()
        b = b.lower()
        if len(a) != len(b):
            return False
        return sorted(a) == sorted(b)
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                count += 1
    return count >= 96