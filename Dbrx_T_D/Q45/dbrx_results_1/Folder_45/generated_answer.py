from collections import defaultdict

def palindromes_between_indices(s: str) -> set[str]:

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def is_valid_char(c: str) -> bool:
        return 'a' <= c.lower() <= 'z'

    def build_pinyin(start: int, end: int) -> str:
        pinyin = ''.join((c.lower() for c in s[start:end + 1] if is_valid_char(c)))
        return pinyin if len(pinyin) >= 4 else ''
    result = set()
    pinyins = defaultdict(set)
    for start in range(5):
        for end in range(start, end + 1)[::-1]:
            pinyin = build_pinyin(start, end)
            if pinyin and is_palindrome(pinyin):
                result.add(pinyin)
                pinyins[pinyin].add((start, end))
    for start, end in pinyins.values():
        for _start in range(start + 1, 5):
            for _end in range(end + 1, end - start + 10)[::-1]:
                pinyin = build_pinyin(_start, _end)
                if pinyin and is_palindrome(pinyin):
                    result.add(pinyin)
    return result