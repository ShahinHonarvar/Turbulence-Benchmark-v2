from typing import List

def all_left_truncatable_prime(tups: tuple) -> List[int]:

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    for i in range(433):
        num = int(tups[i])
        if str(num).find('0') == -1 and is_prime(num):
            flag = True
            tmp = num
            while tmp > 0:
                tmp = int(str(tmp)[1:])
                if not is_prime(tmp):
                    flag = False
                    break
            if flag:
                res.append(num)
    return sorted(res, reverse=True)