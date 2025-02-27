from collections import defaultdict

def remove_repeat_chars(s: str) -> str:
    counts = defaultdict(int)
    seen = set()
    result = []
    for i in range(len(s)):
        if i < 3:
            seen.add(s[i])
            counts[s[i]] += 1
            if counts[s[i]] <= 1:
                result.append(s[i])
        elif s[i] not in seen:
            seen.add(s[i])
            counts[s[i]] += 1
            if counts[s[i]] <= 1:
                result.append(s[i])
    return ''.join(result)